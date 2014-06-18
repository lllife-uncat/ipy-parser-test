module.exports = function(grunt) {

    grunt.initConfig({
        watch: {
            python: {
                files: [
					"**/**.py", "**/**.PY",
					"E:/runtime/generator.env/Template.OLI_Template/Item.Script/**/**.PY",
					"E:/runtime/generator.env/Template.OLI_Template/Item.Script/**/**.py",
				],
                tasks: ["shell"]
            }
        },
        shell: {
            runTest: {
                command: "ipy -m unittest testParser.TestItem"
            }
        },
		pylint: {
			options: {},
			test: {
			}
		}
    });

    grunt.loadNpmTasks("grunt-contrib-watch");
    grunt.loadNpmTasks("grunt-shell");
	grunt.loadNpmTasks("grunt-pylint");

    grunt.registerTask("default", ["watch"]);

};
