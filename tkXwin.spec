Summary:	Some X11 extensions for Tk
Summary(pl):	Ró¿ne rozszerzenia X11 do Tk
Name:		tkXwin
Version:	1.0
Release:	1
License:	distributable
Group:		Development/Languages/Tcl
Source0:	http://beepcore-tcl.sourceforge.net/%{name}-%{version}.tgz
# Source0-md5:	1750b22a9b8e68013083d058562d4b65
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-automake.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gpgme-devel
BuildRequires:	libtool
BuildRequires:	tcl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Some X11 extensions for Tk.

%description -l pl
Ró¿ne rozszerzenia X11 do Tk.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I config
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%{_libdir}/%{name}*
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.so.*.*
