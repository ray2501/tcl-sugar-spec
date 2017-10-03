#
# spec file for package tcl-sugar
#

%define tarname sugar

Name:           tcl-sugar
BuildRequires:  tcl >= 8.4
Version:        0.1
Release:        0
Summary:        Lisp-like macro system for Tcl
Url:            http://wiki.tcl.tk/11155
License:        TCL
Group:          Development/Libraries/Tcl
BuildArch:      noarch
Requires:       tcl >= 8.4
BuildRoot:      %{_tmppath}/%{tarname}-%{version}-build
Source0:        http://www.hping.org/tclsbignum/sugar-0.1.tar.gz

%description
Sugar is a macro system for the Tcl programming language, with a design
very similar to Lisp macros. It provides a way to create Tcl procedures
using the [sugar::proc] command instead of the normal Tcl [proc] command,
and a way to define macros that are expanded inline when the procedure is
created. 

%prep
%setup -q -n %{tarname}

%build

%install
dir=%buildroot%tcl_noarchdir/%tarname%version
mkdir -m755 -p $dir
cp -a %tarname%version/*.tcl $dir

%files
%defattr(-,root,root)
%doc API.txt AUTHORS README example
%tcl_noarchdir/%tarname%version

%changelog

