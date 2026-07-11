%global tl_name plates
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Arrange for plates sections of documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/plates
License:	lppl1.1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/plates.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/plates.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The plates package provides a simple facility for inserting colour
figures in a document when they should be gathered and printed together
as in a book's section of colour plates. The package provides a plate
environment that takes the place of the figure environment for such
colour images.

