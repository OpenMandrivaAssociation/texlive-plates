# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/plates
# catalog-date 2007-01-08 00:37:16 +0100
# catalog-license lppl
# catalog-version 0.1
Name:		texlive-plates
Version:	0.1
Release:	1
Summary:	Arrange for "plates" sections of documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/plates
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/plates.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/plates.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The plates package provides a simple facility for inserting
colour figures in a document when they should be gathered and
printed together as in a book's section of colour plates. The
package provides a plate environment that takes the place of
the figure environment for such colour images.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/plates/endplate.sty
%{_texmfdistdir}/tex/latex/plates/plates.sty
%doc %{_texmfdistdir}/doc/latex/plates/README
%doc %{_texmfdistdir}/doc/latex/plates/plates.pdf
%doc %{_texmfdistdir}/doc/latex/plates/plates.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
