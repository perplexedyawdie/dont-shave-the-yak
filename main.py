from taipy.gui import Gui, Markdown

logo = "assets/logo.png"

"""
ABC Analysis variables
"""
input_abc = ""
input_abc_label = "Drop all the tasks that feel overwhelming here and I'll help you prioritize them!"
pages = {
    "/": Markdown("md/root.md"),
    "ABC-Analysis": Markdown("md/abc.md"),
    "Critical-Path-Method": Markdown("md/cpm.md"),
    "Batch-Processing": Markdown("md/batch-pro.md"),
    "Theory-of-Constraints": Markdown("md/toc.md"),
    "Wellbeing": Markdown("md/wellbeing.md")
}

Gui(pages=pages,css_file="styles.css").run(use_reloader=True)