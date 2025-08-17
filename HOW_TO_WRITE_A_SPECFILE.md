## Creating a Spec

I am *not* an experienced packager, but here are notes on what worked for me.

I used [distrobox](https://github.com/89luca89/distrobox) to have a separate
Fedora installation to install these RPMs on to not pollute my distro. You'll
have to remove the ``~/rpmbuild` dir which gets created when you're done, but
otherwise it's an isolated environment.

The [Fedora Packaging
Tutorial](https://docs.fedoraproject.org/en-US/package-maintainers/Packaging_Tutorial_2_GNU_Hello/)
was the most useful guide for dependencies and advice. I wish there was a
better all-intensive guide to see every macro, but I couldn't find one. The
other good resources were
- [Fedora RPM Macros](https://docs.fedoraproject.org/en-US/packaging-guidelines/RPMMacros/)
- [RPM Packaging Guide](https://rpm-packaging-guide.github.io/)
- and a lot of random stackoverflow questions

You're also welcome to look at the spec files here if you aren't doing anything
too complicated, they're hopefully good examples on how to package a binary!

Nowadays to write a spec, I mainly follow the steps in that Fedora Packaging Tutorial:
- copy one of my existing specs as a template
- update the fields
- open a distrobox with `fedora-packager` installed
- copy the spec file to its own folder for testing
- use `spectool -g <spec-file>` to download the source
- run `fedpkg mockbuild` to build the specfile so far. I do this gradually - first, add an `ls` after the `%autosetup` and see if it works, if not try adding the necessary flags from my other specs until I get the folder structure I want, and continue on
- once I think it's fully built, try installing the rpm in the `results` folder with DNF and test it, if it works it's good to go!
- add the package to my COPR repository

These specfiles are not actually building the packages, I'm just linking
the binaries from Github Releases. If your project pushes a binary directly
to Github Actions, you can do this too! Look at some of the simple specs like
[zellij.spec](specs/zellij.spec) as an example. The key process is
- set the URL to the github repo
- set the Source to the download of the binary you need
- utilize macros like %{version} to make auto-updates possible
- run %autosetup to deal with the source files (and use -c if the download doesn't come with a top level directory)
- have an empty %build section if you don't need to build anything
- run the necessary install commands to install the binary
- list all the files you've installed in %files.

For writing more advanced spec files, I found looking at other spec files to
be useful. You can search up anything in the Fedora repos at [Fedora
Packages](https://packages.fedoraproject.org/), click on Sources, Files, and
you can see the spec file for it. I've picked up some random macros from there.
`fedpkg lint` has also been very useful in finding better ways to do things.

If you don't like `fedpkg`, you can build without it. To test, use `rpmlint
*your spec file*` to lint your file. Once it's good, run `spectool -g -R -f
*your spec file*` to download sources, then `rpmbuild -bb *your spec file*`
to build the rpm. If successful, try installing it with `sudo dnf install ~/
rpmbuild/RPMS/*path to your rpm*`. Try the binary, and if it works you're set!


