selector_to_html = {"a[href=\"#Todolist.Backend.app.create_app\"]": "<dt class=\"sig sig-object py\" id=\"Todolist.Backend.app.create_app\">\n<span class=\"sig-prename descclassname\"><span class=\"pre\">Todolist.Backend.app.</span></span><span class=\"sig-name descname\"><span class=\"pre\">create_app</span></span><span class=\"sig-paren\">(</span><span class=\"sig-paren\">)</span> <span class=\"sig-return\"><span class=\"sig-return-icon\">\u2192</span> <span class=\"sig-return-typehint\"><span class=\"pre\">flask.Flask</span></span></span><a class=\"reference internal\" href=\"../../_modules/Todolist/Backend/app.html#create_app\"><span class=\"viewcode-link\"><span class=\"pre\">[source]</span></span></a></dt><dd><p>Create and configure the Flask application.</p></dd>", "a[href=\"#module-Todolist.Backend.app\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\"><a class=\"reference internal\" href=\"#module-Todolist.Backend.app\" title=\"Todolist.Backend.app\"><code class=\"xref py py-mod docutils literal notranslate\"><span class=\"pre\">Todolist.Backend.app</span></code></a><a class=\"headerlink\" href=\"#module-Todolist.Backend.app\" title=\"Link to this heading\">#</a></h1><p>Project metadata.</p>", "a[href=\"#api\"]": "<h3 class=\"tippy-header\" style=\"margin-top: 0;\">API<a class=\"headerlink\" href=\"#api\" title=\"Link to this heading\">#</a></h3>", "a[href=\"#module-contents\"]": "<h2 class=\"tippy-header\" style=\"margin-top: 0;\">Module Contents<a class=\"headerlink\" href=\"#module-contents\" title=\"Link to this heading\">#</a></h2><h3>Functions<a class=\"headerlink\" href=\"#functions\" title=\"Link to this heading\">#</a></h3>", "a[href=\"#functions\"]": "<h3 class=\"tippy-header\" style=\"margin-top: 0;\">Functions<a class=\"headerlink\" href=\"#functions\" title=\"Link to this heading\">#</a></h3>"}
skip_classes = ["headerlink", "sd-stretched-link"]

window.onload = function () {
    for (const [select, tip_html] of Object.entries(selector_to_html)) {
        const links = document.querySelectorAll(` ${select}`);
        for (const link of links) {
            if (skip_classes.some(c => link.classList.contains(c))) {
                continue;
            }

            tippy(link, {
                content: tip_html,
                allowHTML: true,
                arrow: true,
                placement: 'auto-start', maxWidth: 500, interactive: false,

            });
        };
    };
    console.log("tippy tips loaded!");
};
