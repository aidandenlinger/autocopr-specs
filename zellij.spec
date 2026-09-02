%global debug_package %{nil}

Name: zellij
Version: 0.45.1
Release: 2%{?dist}
Summary: [THIS COPR IS DEPRECATED] A terminal workspace with batteries included

License:    MIT
URL:        https://github.com/zellij-org/zellij
Source:     %{url}/releases/download/v%{version}/%{name}-x86_64-unknown-linux-musl.tar.gz
Source1:    https://raw.githubusercontent.com/zellij-org/zellij/v%{version}/LICENSE.md

%description
This COPR repo is deprecated, please migrate to another.
See https://copr.fedorainfracloud.org/coprs/adenl/github-releases/ for more info.

Zellij is a workspace aimed at developers, ops-oriented people and anyone
who loves the terminal. At its core, it is a terminal multiplexer (similar to
tmux and screen), but this is merely its infrastructure layer. Zellij includes
a layout system, and a plugin system allowing one to create plugins in any
language that compiles to WebAssembly.

%prep
# This source file doesn't have a high level directory, so create one
%autosetup -c
# Get the LICENSE in the build dir
cp %{SOURCE1} .

%build
# Generate shell completions
./%{name} setup --generate-completion bash > %{name}.bash
./%{name} setup --generate-completion zsh > _%{name}
./%{name} setup --generate-completion fish > %{name}.fish

# Generate manpage (https://eddieantonio.ca/blog/2015/12/18/authoring-manpages-in-markdown-with-pandoc/)
pandoc --standalone --to man MANPAGE.md | gzip -c > %{name}.1.gz

%install
install -p -D %{name} %{buildroot}%{_bindir}/%{name}

# Shell completions
install -pvD -m 0644 %{name}.bash %{buildroot}%{bash_completions_dir}/%{name}
install -pvD -m 0644 _%{name} %{buildroot}%{zsh_completions_dir}/_%{name}
install -pvD -m 0644 %{name}.fish %{buildroot}%{fish_completions_dir}/%{name}.fish

%post
cat << 'EOF'
==================================================================
WARNING: The adenl/github-releases Copr repo is DEPRECATED.
It will not host packages for Fedora 45.
Automated updates for Fedora 44 will continue
until Fedora 44 EOL 2027-06-01, but any issues will not be fixed.
Please migrate to another source to acquire `zellij`.
See https://copr.fedorainfracloud.org/coprs/adenl/github-releases/
for more info.
==================================================================
EOF

%files
%{_bindir}/%{name}
%{bash_completions_dir}/%{name}
%{zsh_completions_dir}/_%{name}
%{fish_completions_dir}/%{name}.fish
%license LICENSE.md
