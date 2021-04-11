# pynyin

#### a python utility to perform basic actions on pinyin strings

## Usage
This utility performs basic actions on pinyin strings. It should be considered
a work in progress at this point. The usage string:

```
$ pynyin -h
usage: pynyin [-h] (-t | -r | -a) pinyin

Perform simple actions on pinyin strings

positional arguments:
  pinyin        the pinyin string

optional arguments:
  -h, --help    show this help message and exit
  -t, --tone    get the (next) tone
  -r, --remove  remove tones (preserves other non-ASCII)
  -a, --ascii   convert to ASCII
```

Here's a simple usage example:

```
$ pynyin -t "shànghǎi"
4
$ pynyin -r "shànghǎi"
shanghai
$ pynyin -a "shànghǎi"
shanghai
```

A couple of things to note about this example:
* the `-t,--tone` option only returns the first tone found or 0 if none found
* the `-r,--remove` and `-a,--ascii` options *seem* to do the same thing, but the former preserves other non-ASCII characters whereas the latter only outputs ASCII

Another example that shows different output for `-r` and `-a`:

```
$ ./pynyin -t "lǚchá"
3
$ ./pynyin -r "lǚchá"
lücha
$ ./pynyin -a "lǚchá"
lucha
```

The utility can also be used as a library. For examples of how to do this, have a look at the tests under the _tests_ directory.


## TODOs / Wishlist
* Parse pinyin into syllables and output lists of tones or syllables (with tones preserved or stripped) - I have already planned to do this but haven't had a chance to implementing it yet
* Convert a Chinese character string into a corresponding pinyin string - this will be tricky and probably require tapping into some IME or similar system

