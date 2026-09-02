selector_to_html = {"a[href=\"#submodules\"]": "<h2 class=\"tippy-header\" style=\"margin-top: 0;\">Submodules<a class=\"headerlink\" href=\"#submodules\" title=\"Link to this heading\">#</a></h2>", "a[href=\"Todolist.test.integration.html\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\"><a class=\"reference internal\" href=\"#module-Todolist.test.integration\" title=\"Todolist.test.integration\"><code class=\"xref py py-mod docutils literal notranslate\"><span class=\"pre\">Todolist.test.integration</span></code></a><a class=\"headerlink\" href=\"#module-Todolist.test.integration\" title=\"Link to this heading\">#</a></h1><p>Bundle integration tests in the distribution.</p><p>This facilitates the operational qualification of production\ndeployments.</p>", "a[href=\"Todolist.test.test_example.html\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\"><a class=\"reference internal\" href=\"#module-Todolist.test.test_example\" title=\"Todolist.test.test_example\"><code class=\"xref py py-mod docutils literal notranslate\"><span class=\"pre\">Todolist.test.test_example</span></code></a><a class=\"headerlink\" href=\"#module-Todolist.test.test_example\" title=\"Link to this heading\">#</a></h1><p>Example unit test.</p>", "a[href=\"#subpackages\"]": "<h2 class=\"tippy-header\" style=\"margin-top: 0;\">Subpackages<a class=\"headerlink\" href=\"#subpackages\" title=\"Link to this heading\">#</a></h2>", "a[href=\"#module-Todolist.test\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\"><a class=\"reference internal\" href=\"#module-Todolist.test\" title=\"Todolist.test\"><code class=\"xref py py-mod docutils literal notranslate\"><span class=\"pre\">Todolist.test</span></code></a><a class=\"headerlink\" href=\"#module-Todolist.test\" title=\"Link to this heading\">#</a></h1><p>Bundle functional tests with the distribution.</p><p>This facilitates the operational qualification of production\ndeployments.</p>", "a[href=\"Todolist.test.conftest.html\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\"><a class=\"reference internal\" href=\"#module-Todolist.test.conftest\" title=\"Todolist.test.conftest\"><code class=\"xref py py-mod docutils literal notranslate\"><span class=\"pre\">Todolist.test.conftest</span></code></a><a class=\"headerlink\" href=\"#module-Todolist.test.conftest\" title=\"Link to this heading\">#</a></h1><p>Configure test fixtures.</p>"}
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
