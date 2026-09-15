selector_to_html = {"a[href=\"#submodules\"]": "<h2 class=\"tippy-header\" style=\"margin-top: 0;\">Submodules<a class=\"headerlink\" href=\"#submodules\" title=\"Link to this heading\">#</a></h2>", "a[href=\"tests.conftest.html\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\"><a class=\"reference internal\" href=\"#module-tests.conftest\" title=\"tests.conftest\"><code class=\"xref py py-mod docutils literal notranslate\"><span class=\"pre\">tests.conftest</span></code></a><a class=\"headerlink\" href=\"#module-tests.conftest\" title=\"Link to this heading\">#</a></h1><p>The top-level test configuration file.</p>", "a[href=\"#module-tests\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\"><a class=\"reference internal\" href=\"#module-tests\" title=\"tests\"><code class=\"xref py py-mod docutils literal notranslate\"><span class=\"pre\">tests</span></code></a><a class=\"headerlink\" href=\"#module-tests\" title=\"Link to this heading\">#</a></h1><p>Top-level tests.</p><p>This helps keep selected integration tests outside the source tree.\nContainer images can then perform testing at build time without having\nto mark (and exclude) integration tests that use said container\nimages.</p>"}
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
