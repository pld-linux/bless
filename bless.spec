Summary:	Hex Editor written in GTK#
Summary(pl):	Edytor szesnastkowy napisany w GTK#
Name:		bless
Version:	0.2.3
Release:	1
License:	GPL
Group:		Applications/Editors
Source0:	http://download.gna.org/bless/%{name}-%{version}.tar.gz
# Source0-md5:	b9c70c141a059cd9593ce3b32b828d3b
Source1:	%{name}.desktop
Patch0:		%{name}-DESTDIR.patch
URL:		http://home.gna.org/bless/
BuildRequires:	dotnet-gtk-sharp-devel >= 1.0
BuildRequires:	mono-csharp >= 1.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bless aims to be a fast and customizable hex (binary) editor.

%description -l pl
Bless stara siê byæ szybkim i konfigurowalnym edytorem szesnastkowym
(binarnym).

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS Changelog NEWS README doc/user
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*.exe
%{_desktopdir}/*
