Title: Configuring Xmonad
Date: 2014-02-09 15:55
Category: Dotfiles 
Author: William Mak
Summary: Going over how I've set up xmonad

So after having a bunch of wireless issues and poorly installing wicd on Linux mint I've decided to revisit using arch linux. I then spent a day fumbling around in arch until I finally had it running with [xmonad](http://xmonad.org/) and [xmobar](http://projects.haskell.org/xmobar/). I've also posted my dotfiles on [github](https://github.com/wmak/dotfiles) if anyone else wants to configure their setup with them as well. Just note that I've added some keybindings for colemak but I think most of the qwerty bindings are still there.

# xmobar
Having xmonad and xmobar start together actually took a long time to set up. Originally I had xmonad run xmobar itself as per the [arch wiki](https://wiki.archlinux.org/index.php/Xmonad#Using_xmobar_with_xmonad). Which had xinitrc only need to run `exec xmonad`, but because of a [bug](http://www.haskell.org/haskellwiki/Xmonad/Frequently_asked_questions#XMonad_is_frozen.21) in xmonad if you change windows... or watch a video... or just use xmonad it will freeze up and become completely unusable. So instead I configured xmonad to leave a gap at the top of the screen and had xmobar run seperately. At first I tried having xinitrc do `exec xmonad | xmobar` which seemed to work perfectly until I had to quit, at which point xmonad would completely freeze up and become unresponsive. In the end I figured I could run xmobar seperately in the background so the final xinitrc runs `xmobar &` right before executing xmonad

# xmonad
Currently xmonad isn't configured all too much most of the default configs are perfect for me, but I set up the colours from a them I found on [kuler](https://kuler.adobe.com/Vintage-Color-color-theme-3369015/edit/?copy=true&base=2&rule=Custom&selected=0&name=Copy%20of%20Vintage%20Color&mode=hsv&rgbvalues=0.9411764705882353,0.2980392156862745,0.08627450980392157,0.8588235294117647,0.8588235294117647,0.8156862745098039,0.9294117647058824,0.7411764705882353,0.12156862745098039,0.2980392156862745,0.6901960784313725,0.611764705882353,0.19215686274509805,0.23137254901960785,0.2901960784313726&swatchOrder=0,1,2,3,4_), modified the layout to fit xmobar, and added some custom keyboard shortcuts.
