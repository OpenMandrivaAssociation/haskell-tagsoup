%define module tagsoup

Name: haskell-%{module}
Version: 0.6
Release: %mkrel 3
Summary: Parsing and extracting information from (possibly malformed) HTML documents
Group: Development/Other
License: BSD3
Url: http://hackage.haskell.org/package/tagsoup
Source: http://hackage.haskell.org/packages/archive/%{module}/%{version}/%{module}-%{version}.tar.gz
BuildRoot: %_tmppath/%name-%version-%release-root
BuildRequires: ghc
BuildRequires: haddock
BuildRequires: haskell-macros
BuildRequires: curl-devel

%description
TagSoup is a library for extracting information out of unstructured HTML
code, sometimes known as tag-soup. The HTML does not have to be well formed,
or render properly within any particular framework. This library is for
situations where the author of the HTML is not cooperating with the person
trying to extract the information, but is also not trying to hide the
information.

%prep
%setup -q -n %{module}-%{version}

%build
%_cabal_build

%_cabal_genscripts

%check
%_cabal_check

%install
%_cabal_install

rm -fr %{buildroot}/%_datadir/*/doc/

%_cabal_rpm_gen_deps

%_cabal_scriptlets

%files
%defattr(-,root,root)
%_docdir/%{module}-%{version}
%_libdir/*
%_bindir/%{module}
%_cabal_rpm_files

%clean
rm -fr %buildroot


