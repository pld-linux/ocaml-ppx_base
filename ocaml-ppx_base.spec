#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Base set of ppx rewriters
Summary(pl.UTF-8):	Podstawowy zbiór modułów przepisujących ppx
Name:		ocaml-ppx_base
Version:	0.14.0
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/janestreet/ppx_base/tags
Source0:	https://github.com/janestreet/ppx_base/archive/v%{version}/ppx_base-%{version}.tar.gz
# Source0-md5:	fb673a26794a28723e82707fa333f365
URL:		https://github.com/janestreet/ppx_base
BuildRequires:	ocaml >= 1:4.04.2
BuildRequires:	ocaml-base-devel >= 0.14
BuildRequires:	ocaml-base-devel < 0.15
BuildRequires:	ocaml-dune >= 2.0.0
BuildRequires:	ocaml-ppx_cold-devel >= 0.14
BuildRequires:	ocaml-ppx_cold-devel < 0.15
BuildRequires:	ocaml-ppx_compare-devel >= 0.14
BuildRequires:	ocaml-ppx_compare-devel < 0.15
BuildRequires:	ocaml-ppx_enumerate-devel >= 0.14
BuildRequires:	ocaml-ppx_enumerate-devel < 0.15
BuildRequires:	ocaml-ppx_hash-devel >= 0.14
BuildRequires:	ocaml-ppx_hash-devel < 0.15
BuildRequires:	ocaml-ppx_js_style-devel >= 0.14
BuildRequires:	ocaml-ppx_js_style-devel < 0.15
BuildRequires:	ocaml-ppx_sexp_conv-devel >= 0.14
BuildRequires:	ocaml-ppx_sexp_conv-devel < 0.15
BuildRequires:	ocaml-ppxlib-devel >= 0.11.0
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
ppx_base is the set of ppx rewriters used for Base.

This package contains files needed to run bytecode executables using
ppx_base library.

%description -l pl.UTF-8
ppx_base to zbiór modułów przepisujących ppx używanych do Base.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki ppx_base.

%package devel
Summary:	Base set of ppx rewriters - development part
Summary(pl.UTF-8):	Podstawowy zbiór modułów przepisujących ppx - część programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
Requires:	ocaml-base-devel >= 0.14
Requires:	ocaml-ppx_cold-devel >= 0.14
Requires:	ocaml-ppx_compare-devel >= 0.14
Requires:	ocaml-ppx_enumerate-devel >= 0.14
Requires:	ocaml-ppx_hash-devel >= 0.14
Requires:	ocaml-ppx_js_style-devel >= 0.14
Requires:	ocaml-ppx_sexp_conv-devel >= 0.14
Requires:	ocaml-ppxlib-devel >= 0.11.0

%description devel
This package contains files needed to develop OCaml programs using
ppx_base library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki ppx_base.

%prep
%setup -q -n ppx_base-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/ppx_base/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/ppx_base

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.md
%attr(755,root,root) %{_bindir}/ppx-base
%dir %{_libdir}/ocaml/ppx_base
%attr(755,root,root) %{_libdir}/ocaml/ppx_base/ppx.exe
%{_libdir}/ocaml/ppx_base/META
%{_libdir}/ocaml/ppx_base/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/ppx_base/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/ppx_base/*.cmi
%{_libdir}/ocaml/ppx_base/*.cmt
%if %{with ocaml_opt}
%{_libdir}/ocaml/ppx_base/ppx_base.a
%{_libdir}/ocaml/ppx_base/*.cmx
%{_libdir}/ocaml/ppx_base/*.cmxa
%endif
%{_libdir}/ocaml/ppx_base/dune-package
%{_libdir}/ocaml/ppx_base/opam
