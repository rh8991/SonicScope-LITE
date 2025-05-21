from nicegui import app, ui
import signal_tools as tools 
import plotly.graph_objects as go
import signal_processing as sp
import config

INPUT_FILENAME ,OUTPUT_FILENAME = config.INPUT_FILENAME ,config.OUTPUT_FILENAME

fig_time = config.fig_time
fig_freq = config.fig_freq

# === Functions ===

def clear_plots():
    print("Cleaning plots")
    fig_time.data = []
    fig_freq.data = []

    plot_time.update()
    plot_freq.update()

    ui.notify('גרפים נוקו')

# === GUI ===


    
with ui.row().classes('items-start'):
    with ui.column().classes('items-left justify-center q-pa-md gap-4'):
        with ui.row().classes('items-center justify-center'):
            ui.image(config.logo).classes('w-20 h-20')
            ui.label('SonicScope').classes('text-h6')
        
        with ui.row().classes('items-center justify-center'):   
            ui.label('כניסה').classes('text-h6')
            
        with ui.row().classes('items-center justify-center'):
            ui.button('🔴 הקלטה', on_click=lambda: (
                ui.notify('מקליט...'),
                tools.record_audio(), 
                ui.notify('הקלטה הסתיימה')))
            ui.button('▶️ הפעל', on_click=lambda: (tools.play_signal(INPUT_FILENAME), ui.notify('מפעיל כניסה')))
            ui.button('📈 שרטט', on_click=lambda: (ui.notify('משרטט'), tools.plot_Input_signal(), plot_time.update()))
            
            #TODO fix clear button
            
            ui.button('🗑️ Clear', on_click=clear_plots)
                
                
        with ui.row().classes('items-center justify-center' ):
            ui.upload(on_upload=tools.upload_signal, label='🎵 העלה קובץ ')

        with ui.row().classes('items-left justify-center'):
            ui.label('יציאה').classes('text-h6')
            
        with ui.row().classes('items-center justify-center'):
            scale_in = ui.number(label='שינוי עוצמה', value=1, min=0, max=2, step=0.1).classes('w-20')
            #t_shift_in = ui.number(label='Time shifting [ms]',value=0, min=0, step=1)
            
            ui.button('צור', on_click=lambda: (
                #sp.time_shift(t_shift_in.value), print(f"TIME SHIFTING {t_shift_in.value}") if t_shift_in.value > 0 else None, #! TODO: fix time shifting
                sp.scaling(scale_in.value), print(f"SCALING {scale_in.value}") if scale_in.value != 1 else None,
                tools.add_output(),
                plot_time.update()))
            
            ui.button('▶️ הפעל', on_click=lambda: (tools.play_signal(OUTPUT_FILENAME), ui.notify('מפעיל מוצא')))
            
        with ui.row().classes('items-center justify-center'):
            ui.button('תדר', on_click=lambda: (
                print("applying FFT..."),
                sp.fft(),
                ui.notify('מחשב FFT'),
                plot_freq.update(),
                ))
                
                    
    with ui.column().classes('q-pa-md'):
        with ui.tabs() as tabs:
            ui.tab('זמן', icon = 'timeline')
            ui.tab('תדר', icon = 'timeline')
            
        with ui.tab_panels(tabs, value='זמן'):#.classes('w-full'):
            with ui.tab_panel('זמן'):
                fig_time.update_layout(
                    legend=dict(orientation='h', yanchor='bottom', y = -0.3, xanchor='right', x=1),
                    margin=dict(l = 0, r = 0, t = 0, b = 0),
                    xaxis_title = 'זמן (s)',
                    yaxis_title = 'עוצמה')
                    
                plot_time = ui.plotly(fig_time).classes('w-full h-80')
                            
            with ui.tab_panel('תדר'):
                fig_freq.update_layout(
                    legend=dict(orientation='h', yanchor='bottom', y=-0.3, xanchor='right', x=1),
                    margin=dict(l=0, r=0, t=0, b=0),
                    xaxis_title='תדר (Hz)',
                    yaxis_title='עוצמת התדר')
                
                plot_freq = ui.plotly(fig_freq).classes('w-full h-80')
        
          
with ui.footer().classes('items-center justify-center q-pa-none q-mt-none').style('height: 30px;'):
    ui.label('SonicScope - Developed by Ronel Herzass').classes('text-caption q-mb-none').style('line-height: 1; margin: 0; padding: 0')


ui.run()
