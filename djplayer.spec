
%define tname	%(echo %{name}|tr -d er)
%define	tver	%(echo %{version}|tr -d .)

Summary:	DJ's Player - simple CD Audio player
Summary(pl):	DJ's Player - prosty odtwarzacz CD Audio
Name:		djplayer
Version:	1.6
Release:	1
License:	GPL v2
Group:		Applications/Sound
Source0:	http://tpnet.linux.tucows.com/files/console/media/%{tname}%{tver}.tgz
# Source0-md5:	d68b90cc3e20303efdfb6afdc2af8944
Patch0:		%{name}-fixncurses.patch
URL:		http://linux.tucows.com/preview/56677.html
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DJ's Player is a simple CD player for Linux and compatible operating
systems.

%description -l pl
DJ's Player jest prostym odtwarzaczem CD pod linuxa i kompatybilnych
systemów operacyjnych.

%prep
%setup -q -n %{name}
%patch0 -p1
%build

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
