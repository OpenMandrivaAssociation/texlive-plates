Name:		texlive-plates
Version:	15878
Release:	2
Summary:	Arrange for "plates" sections of documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/plates
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/plates.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/plates.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The plates package provides a simple facility for inserting
colour figures in a document when they should be gathered and
printed together as in a book's section of colour plates. The
package provides a plate environment that takes the place of
the figure environment for such colour images.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/plates/endplate.sty
%{_texmfdistdir}/tex/latex/plates/plates.sty
%doc %{_texmfdistdir}/doc/latex/plates/README
%doc %{_texmfdistdir}/doc/latex/plates/plates.pdf
%doc %{_texmfdistdir}/doc/latex/plates/plates.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
