Summary:	Hex Editor written in GTK#
Summary(pl.UTF-8):   Edytor szesnastkowy napisany w GTK#
Name:		bless
Version:	0.4.1
Release:	1
License:	GPL
Group:		Applications/Editors
Source0:	http://download.gna.org/bless/%{name}-%{version}.tar.gz
# Source0-md5:	a3551ebecda11b115e98608894f5c0ec
Source1:	%{name}.desktop
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-help.patch
Patch2:		%{name}-glyphs_overlap.patch
URL:		http://home.gna.org/bless/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-gtk-sharp2-devel >= 1.9.5
BuildRequires:	libtool
BuildRequires:	mono-csharp >= 1.1.4
BuildRequires:	mono-devel >= 1.0
BuildRequires:	pkgconfig
BuildRequires:	scrollkeeper
Requires(post,postun):	desktop-file-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bless aims to be a fast and customizable hex (binary) editor.

%description -l pl.UTF-8
Bless stara się być szybkim i konfigurowalnym edytorem szesnastkowym
(binarnym).

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--without-scrollkeeper
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
mv $RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}/data/help_script.sh $RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}/bin

%find_lang %{name} --all-name --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post
%update_desktop_database_post

%postun
%scrollkeeper_update_postun
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}-%{version}
%dir %{_libdir}/%{name}-%{version}/bin
%attr(755,root,root) %{_libdir}/%{name}-%{version}/bin/*
%{_libdir}/%{name}-%{version}/data
%{_desktopdir}/*.desktop
%{_omf_dest_dir}/%{name}
%{_pixmapsdir}/*
