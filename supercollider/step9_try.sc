var argv = thisProcess.argv, mal = MAL9.new;
"REAL OUTPUT HERE".postln;
if (argv.notEmpty) {
	mal.rep("(load-file \"%\")".format(argv[0]));
} { mal.repl };
exit(0);