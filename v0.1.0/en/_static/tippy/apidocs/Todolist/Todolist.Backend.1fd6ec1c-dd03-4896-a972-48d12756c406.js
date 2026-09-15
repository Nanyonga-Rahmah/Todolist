selector_to_html = {"a[href=\"#module-Todolist.Backend\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\"><a class=\"reference internal\" href=\"#module-Todolist.Backend\" title=\"Todolist.Backend\"><code class=\"xref py py-mod docutils literal notranslate\"><span class=\"pre\">Todolist.Backend</span></code></a><a class=\"headerlink\" href=\"#module-Todolist.Backend\" title=\"Link to this heading\">#</a></h1><p>Backend api.</p>", "a[href=\"#submodules\"]": "<h2 class=\"tippy-header\" style=\"margin-top: 0;\">Submodules<a class=\"headerlink\" href=\"#submodules\" title=\"Link to this heading\">#</a></h2>", "a[href=\"Todolist.Backend.app.html\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\"><a class=\"reference internal\" href=\"#module-Todolist.Backend.app\" title=\"Todolist.Backend.app\"><code class=\"xref py py-mod docutils literal notranslate\"><span class=\"pre\">Todolist.Backend.app</span></code></a><a class=\"headerlink\" href=\"#module-Todolist.Backend.app\" title=\"Link to this heading\">#</a></h1><p>Project metadata.</p>"}
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
