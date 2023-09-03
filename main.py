from taipy.gui import Gui, Markdown, invoke_long_callback, notify
from chat_gpt import abc_analyser, task_batcher, critical_path_finder, mood_booster
logo = "assets/logo.png"


"""
General Variables
"""

"""
ABC Analysis variables
"""
abc_active = True
input_abc = ""
input_abc_label = "Drop all the tasks that feel overwhelming here and I'll help you prioritize them!"
output_abc_analysis = ""
def abc_status(state, status, result):
    if isinstance(status, bool):
        if status:
            notify(state, "success", f"Query complete!")
            state.output_abc_analysis = result
            state.abc_active=True
        else:
            notify(state, "error", f"The query has failed somehow.")
    else:
        notify(state, "info", f"Running query! Hold tight...")

def run_analysis(state):
    if state.abc_active == False:
        notify(state, "warning", "Please wait until this query is complete!")
    if len(state.input_abc) > 50 and state.abc_active == True:
        state.abc_active=False
        invoke_long_callback(state, abc_analyser, [state.input_abc], abc_status, [], period=3000)

"""
Batch Processing variables
"""
batch_pro_active = True
input_batch_pro = ""
input_batch_pro_label = "Drop all the tasks that feel overwhelming here and I'll help you to batch them in ways that make it less harder to finish them!"
output_batch_pro_analysis = ""
def batch_pro_status(state, status, result):
    if isinstance(status, bool):
        if status:
            notify(state, "success", f"Query complete!")
            state.output_batch_pro_analysis = result
            state.batch_pro_active = True
        else:
            notify(state, "error", f"The query has failed somehow.")
    else:
        notify(state, "info", f"Running query! Hold tight...")
def run_batching(state):
    if state.batch_pro_active == False:
        notify(state, "warning", "Please wait until this query is complete!")
    if len(state.input_batch_pro) > 50 and state.batch_pro_active == True:
        state.batch_pro_active = False
        invoke_long_callback(state, task_batcher, [state.input_batch_pro], batch_pro_status, [], period=3000)

"""
Critical Path Method variables
"""
cpm_active = 1
input_cpm = ""
input_cpm_label = "Drop all the tasks that feel overwhelming here and I'll help you to organize them based on the amount of dedicated time each requires!"
output_cpm_analysis = ""
def cpm_status(state, status, result):
    if isinstance(status, bool):
        if status:
            notify(state, "success", f"Query complete!")
            state.output_cpm_analysis = result
            state.cpm_active = True
        else:
            notify(state, "error", f"The query has failed somehow.")
    else:
        notify(state, "info", f"Running query! Hold tight...")
def run_cpm(state):
    if state.cpm_active == False:
        notify(state, "warning", "Please wait until this query is complete!")
    if len(state.input_cpm) > 50 and state.cpm_active == True:
        state.cpm_active = False
        invoke_long_callback(state, critical_path_finder, [state.input_cpm], cpm_status, [], period=3000)

"""
Wellbeing variables
"""
input_wellbeing = ""
input_wellbeing_label = "Drop what you're doing and take a short break to boost your mood! Just tell me how much time you've got to spare :)"
output_wellbeing_analysis = ""
def wellbeing_status(state, status, result):
    if isinstance(status, bool):
        if status:
            notify(state, "success", f"Query complete!")
            state.output_wellbeing_analysis = result
        else:
            notify(state, "error", f"The query has failed somehow.")
    else:
        notify(state, "info", f"Running query! Hold tight...")
def run_wellbeing(state):
    if len(state.input_wellbeing) > 50:
        invoke_long_callback(state, mood_booster, [state.input_wellbeing], wellbeing_status, [], period=3000)

pages = {
    "/": Markdown("md/root.md"),
    "ABC-Analysis": Markdown("md/abc.md"),
    "Critical-Path-Method": Markdown("md/cpm.md"),
    "Batch-Processing": Markdown("md/batch-pro.md"),
    # "Wellbeing": Markdown("md/wellbeing.md")
}

main = Gui(pages=pages,css_file="styles.css").run(title="Don't Shave The Yak", host="0.0.0.0", run_browser=False, run_server=False)