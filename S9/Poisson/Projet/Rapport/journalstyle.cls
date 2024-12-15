\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{journalstyle}[2024/11/19 Custom journal style]

\LoadClass[11pt,twoside]{article}

% Packages
\RequirePackage[utf8]{inputenc}
\RequirePackage[T1]{fontenc}
\RequirePackage{lmodern}
\RequirePackage[english]{babel}
\RequirePackage{amsmath}
\RequirePackage{amsfonts}
\RequirePackage{amssymb}
\RequirePackage{graphicx}
\RequirePackage{xcolor}
\RequirePackage{mathtools}
\RequirePackage{fancyhdr}
\RequirePackage{enumitem}
\RequirePackage{tcolorbox}
\RequirePackage{stmaryrd}
\RequirePackage{dsfont}
\RequirePackage{multicol}
\RequirePackage{csquotes}
\RequirePackage{float}
\RequirePackage[hyperindex=true, hyperfigures=false, linktocpage=true, colorlinks=true, linkcolor=blue, urlcolor=blue]{hyperref}
\RequirePackage{pgf, tikz}
\usetikzlibrary{shapes.misc}
\RequirePackage[linesnumbered,ruled,vlined]{algorithm2e}
\RequirePackage[text={18cm,23cm},centering]{geometry}
\RequirePackage[backend=biber, sorting=none]{biblatex}


% Bibliography
\addbibresource{references.bib}

% Header and footer
\pagestyle{fancy}
\fancyhf{} % Clear all header and footer fields
\fancyhead{} % Clear header
\fancyfoot{} % Clear footer

% Custom headers and footers
\fancyhead[LE,RO]{\bfseries \thepage} % Bold page number on the left for even and right for odd pages
\renewcommand{\headrulewidth}{0pt}    % Remove the line at the top

% Footer
\fancyfoot[C]{\fontsize{9}{11}\selectfont \footertext}
\setlength{\headheight}{14pt}

% Redefine \maketitle
\renewcommand{\maketitle}{
    \noindent
    \thispagestyle{empty}

    % Logos and title in one row
    \begin{minipage}[t]{0.3\textwidth} % Left side: Logos
        \includegraphics[height=0.8cm]{src/inp_n7.png} \\[0.5cm]
        \includegraphics[height=0.8cm]{src/insa_toulouse.png}
    \end{minipage}
    \hfill
    \begin{minipage}[t]{0.7\textwidth} % Right side: Title
        {\raggedleft\huge\bfseries\@title\par} % Dynamically fetches title
    \end{minipage}

    \vspace{1cm} % Space between logos/title and authors

    % Authors aligned to the left
    {\large\bfseries\@author\par} % Dynamically fetches authors

    \vspace{0.5cm} % Space before horizontal line

    % Horizontal line
    \hrule

    \setlength{\columnsep}{1cm}
    \begin{multicols}{2}
    
    \vspace{1cm} % Space after horizontal line
}



% Define the function to create a code box
\newcommand{\code}[1]{%
    \begin{tcolorbox}[colback=black!10!white,colframe=black]
        #1
    \end{tcolorbox}
}

% Begin the document
\AtEndDocument{
    \end{multicols}
    \thispagestyle{fancy}
}