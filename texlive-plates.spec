# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/plates
# catalog-date 2007-01-08 00:37:16 +0100
# catalog-license lppl
# catalog-version 0.1
Name:		texlive-plates
Version:	0.1
Release:	10
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.1-2
+ Revision: 754979
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.1-1
+ Revision: 719274
- texlive-plates
- texlive-plates
- texlive-plates
- texlive-plates

