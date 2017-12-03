# Alyke: Finding duplicate files.

Basic useful feature list:

 * Configurable, using settings file or command line.
 * Implementation includes a multiprocess variant for distributed processing.
 * Output on console or log file.
 * Extensible to include in the future, web crawling and application specific content matching for example audio or images.


Configuration in settings.py

```python
config = {
    "crawler_type": "disk",
    "base_path": "/home/test/Downloads/",
    "log_level": logging.DEBUG
}
```

### Alyke: Requirements / How to run?

 * Python 3.5 +
 * Install dependencies in requirements.txt
 * Update configuration file settings.py or alternately, pass command line parameters.
 * Execute script main.py


### Alyke: Variants

There are 3 branches, each implement a slightly different variant:

 * master: Single process variant, that prints duplicates of files during iteration.
 * multiprocess: Multi-Process variant that can be extended to become multi-system using python multiprocessing manager for heavy processing.
 * pretty_print: That outputs duplicate files in groups, but outputs nothing during iteration and uses more memory to save results.

### Design Patterns in use

* Abstract Factory
* Iterable
* Strategy


