%define __spec_install_post %{nil}
%define debug_package %{nil}
%define __os_install_post %{_dbpath}/brp-compress
%define _builddir ./
%define _sourcedir ./
%define _rpmdir ./

Summary: Collection of video tools
Name: video-gadgets
Version: 1.0.0
Release: 1
License: MIT
Group: Development/Tools
URL: https://github.com/m1tk4/video-gadgets

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

Requires: dejavu-sans-mono-fonts ffmpeg

%description
%{summary}

%prep
# nothing to prep

%build
# nothing to build

%install
rm -rf %{buildroot}
install --mode=755 -D hdbars %{buildroot}%{_bindir}/hdbars

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/hdbars

%changelog
* Sat Feb 12 2022 Dimitri Tarassenko <mitka@mitka.us> 1.0-1
- First Build