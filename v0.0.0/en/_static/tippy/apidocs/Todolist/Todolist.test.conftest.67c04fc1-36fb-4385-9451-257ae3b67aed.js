selector_to_html = {"a[href=\"#module-Todolist.test.conftest\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\"><a class=\"reference internal\" href=\"#module-Todolist.test.conftest\" title=\"Todolist.test.conftest\"><code class=\"xref py py-mod docutils literal notranslate\"><span class=\"pre\">Todolist.test.conftest</span></code></a><a class=\"headerlink\" href=\"#module-Todolist.test.conftest\" title=\"Link to this heading\">#</a></h1><p>Configure test fixtures.</p>"}
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
