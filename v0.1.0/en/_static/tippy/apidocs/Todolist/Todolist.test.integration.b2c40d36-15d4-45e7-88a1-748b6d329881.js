selector_to_html = {"a[href=\"#module-Todolist.test.integration\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\"><a class=\"reference internal\" href=\"#module-Todolist.test.integration\" title=\"Todolist.test.integration\"><code class=\"xref py py-mod docutils literal notranslate\"><span class=\"pre\">Todolist.test.integration</span></code></a><a class=\"headerlink\" href=\"#module-Todolist.test.integration\" title=\"Link to this heading\">#</a></h1><p>Bundle integration tests in the distribution.</p><p>This facilitates the operational qualification of production\ndeployments.</p>"}
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
