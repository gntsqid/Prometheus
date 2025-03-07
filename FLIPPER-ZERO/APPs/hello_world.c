#include <furi.h>
#include <gui/gui.h>

/* Main application entry point */
int32_t hello_world_app(void* p) {
    UNUSED(p);

    // Allocate a viewport for rendering
    ViewPort* viewport = view_port_alloc();

    // Draw callback for the viewport
    void draw_callback(Canvas* canvas, void* context) {
        UNUSED(context);
        canvas_clear(canvas);
        // Display "Hello, World!" centered on the screen
        canvas_draw_str_aligned(
            canvas, 64, 32, AlignCenter, AlignCenter, "Hello, World!"
        );
    }

    // Input callback for handling user interactions
    void input_callback(InputEvent* input_event, void* context) {
        FuriMessageQueue* event_queue = context;
        furi_message_queue_put(event_queue, input_event, FuriWaitForever);
    }

    // Set the callbacks for the viewport
    view_port_draw_callback_set(viewport, draw_callback, NULL);

    // Create a message queue for handling input
    FuriMessageQueue* event_queue = furi_message_queue_alloc(8, sizeof(InputEvent));

    // Assign input callback to the viewport
    view_port_input_callback_set(viewport, input_callback, event_queue);

    // Access the GUI and attach the viewport
    Gui* gui = furi_record_open("gui");
    gui_add_view_port(gui, viewport, GuiLayerFullscreen);

    // Event loop: Wait for the back button to be pressed
    InputEvent event;
    while(1) {
        furi_check(furi_message_queue_get(event_queue, &event, FuriWaitForever) == FuriStatusOk);
        if(event.type == InputTypePress && event.key == InputKeyBack) {
            break;
        }
    }

    // Clean up resources
    gui_remove_view_port(gui, viewport);
    view_port_free(viewport);
    furi_message_queue_free(event_queue);
    furi_record_close("gui");

    return 0;
}
