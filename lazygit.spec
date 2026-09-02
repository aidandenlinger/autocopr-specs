# Taken from RelativeSure's repo, thank you!
# https://github.com/RelativeSure/autocopr/blob/54ebe5d5ed94d14aad2bc021507b370d508cc622/specs/lazygit.spec
%global debug_package %{nil}

Name:    lazygit
Version: 0.64.1
Release: 2%{?dist}
Summary: [THIS COPR IS DEPRECATED] simple terminal UI for git commands

License: MIT
URL: https://github.com/jesseduffield/lazygit
Source: %{url}/releases/download/v%{version}/%{name}_%{version}_Linux_x86_64.tar.gz

%description
This COPR repo is deprecated, please migrate to another.
See https://copr.fedorainfracloud.org/coprs/adenl/github-releases/ for more info.

%{summary}

%prep
%autosetup -c

%build

%install
install -p -D %{name} %{buildroot}%{_bindir}/%{name}

%post
cat << 'EOF'
==================================================================
WARNING: The adenl/github-releases Copr repo is DEPRECATED.
It will not host packages for Fedora 45.
Automated updates for Fedora 44 will continue
until Fedora 44 EOL 2027-06-01, but any issues will not be fixed.
Please migrate to another source to acquire `lazygit`.
See https://copr.fedorainfracloud.org/coprs/adenl/github-releases/
for more info.
==================================================================

EOF
%files
%{_bindir}/%{name}
%license LICENSE
