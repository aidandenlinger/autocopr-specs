# AutoCOPR Specs

[![Update spec files](https://github.com/aidandenlinger/autocopr-specs/actions/workflows/update.yml/badge.svg)](https://github.com/aidandenlinger/autocopr-specs/actions/workflows/update.yml)

Specfiles for my [COPR repo], which hosts binaries from Github Releases. Uses my
project [AutoCOPR] to automate updates. **UPDATES ARE AUTOMATED, USE AT YOUR OWN RISK.**

## Background

[Fedora](https://fedoraproject.org/) is a Linux distribution that uses
the [`dnf`](https://docs.fedoraproject.org/en-US/quick-docs/dnf/) package
manager to install, update, and remove packages/software.
[Copr](https://copr.fedorainfracloud.org/) (which stands for Community
Projects) is a build system that takes a
[SPEC file](https://rpm-packaging-guide.github.io/#what-is-a-spec-file) and
builds an [RPM package](https://rpm-packaging-guide.github.io/#what-is-an-rpm)
that can be installed with `dnf`. COPR provides an easy way to integrate user
packages that aren't in the default Fedora repos into the Fedora package
management system.

There are a few Rust CLI tools I like to use that aren't in the default
repository (you can read more about some of the interesting challenges
that come with packaging Rust applications
[here](https://lwn.net/Articles/912202/)). There are some wonderful COPR repos
maintained by others (thank you to [Varlad](https://gitlab.com/VarLad/rpm-specs)
and [Atim](https://copr.fedorainfracloud.org/coprs/atim)), but having to wait
for the version to be manually bumped screamed for an automated solution.

These specs use the binary packages provided by the project mantainers to make
updates resilient, since they already built it, as well as not waste energy
compiling something that is already compiled. However, this requires that you
trust the project maintainers to provide correct binaries. If you don't, please
do not use this repository. (Although feel free to build your own system with
[AutoCOPR]!)

There are several valid alternatives to a repo like this:
- [`cargo-binstall`](https://github.com/cargo-bins/cargo-binstall) or
  installing from source with
  [`cargo install`](https://doc.rust-lang.org/cargo/commands/cargo-install.html)
  would use `cargo` as a package manager to download and update Rust
  programs. This is more idiomatic and certainly easier! However, for me I
  really value having one source of updates for my system so I don't need to
  remember all the different sources, so integrating with `dnf` is ideal.

- There are other COPR repositories that build these programs. You can go to
  [Copr](https://doc.rust-lang.org/cargo/commands/cargo-install.html), type in
  a program name, hit the arrow to filter for "package name", and go explore the
  projects and repositories! *Be sure to check a build for its spec file to see
  what it's doing!* These often build the packages from source and are actually
  maintained by humans, which should provide a crucial layer of security and
  insurance that the package builds and doesn't mess anything up! However, they
  can also take a bit longer to update and I will take any opportunity to
  over-engineer a solution for something that is barely a problem.

## Install

> [!WARNING]
> This repository is not checked by humans! It automatically updates when a new Github release is out and packages the binary package. If this repo or the source projects are compromised, this repo will blindly push that software. Check all updates before installing them on your system. By adding this repo and installing any packages, you are trusting the source project, me, and my code. If you do not trust this chain, please make your own autoCOPR or use an alternative solution.

To add this [COPR repo] on a Fedora x86_64 system, run

```bash
sudo dnf copr enable adenl/github-releases
```

## Usage

> [!WARNING]
> This repository is not checked by humans! It automatically updates when a new Github release is out and packages the binary package. If this repo or the source projects are compromised, this repo will blindly push that software. Check all updates before installing them on your system. By adding this repo and installing any packages, you are trusting the source project, me, and my code. If you do not trust this chain, please make your own autoCOPR or use an alternative solution.

The [COPR repo] lists all the available packages under the `Packages` tab, or you can look through
the specfiles in this repo yourself.

With the repository installed, you can install any package with a specfile from
`dnf` - commands like `sudo dnf install zellij` or `sudo dnf remove zellij` will
work as expected and you will receive updates through the normal dnf mechanism
(typically GNOME Software/KDE Discover or `sudo dnf upgrade`).

## Removed Packages
- 11/17/23: `helix` [has been removed from this repo](https://github.com/aidandenlinger/autocopr/commit/dfc973e8dce1294c9883906342fed5a3e21dba86)
  as [it is in the official Fedora repos](https://packages.fedoraproject.org/pkgs/helix/helix/).

## Thanks
- [VarLad](https://gitlab.com/VarLad/rpm-specs) for writing the original
  [Zellij](https://zellij.dev/) and [Helix](https://helix-editor.com/) specs!
- [Atim](https://copr.fedorainfracloud.org/coprs/atim/starship/) for writing the
  original [Starship](https://starship.rs/) spec!

## Contributing
I'm not accepting contributions, as this is my personal repository. I do not
feel comfortable hosting software that I do not use myself. Please feel free
to utilize the [AutoCOPR] project to make your own repository though!

## License
MIT

[AutoCOPR]: https://github.com/aidandenlinger/autocopr
[COPR repo]: https://copr.fedorainfracloud.org/coprs/adenl/github-releases/
