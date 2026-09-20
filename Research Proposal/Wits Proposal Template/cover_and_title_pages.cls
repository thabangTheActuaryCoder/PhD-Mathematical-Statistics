\ProvidesClass{cover_and_title_pages}[2026/09/20 Wits Statistics and Actuarial Science Proposal]

% Adapted from the BITM LaTeX Proposal Template v4 (eduankotze/BITM), which is
% a University of the Free State, Department of Computer Science & Informatics
% template. Structure and typographic settings are kept; the branding is
% rebuilt for the University of the Witwatersrand. The UFS cover artwork is
% not reused: the cover here is drawn in TikZ from the official Wits palette.

\documentclass[12pt]{article}

\RequirePackage{fontspec}
\RequirePackage{graphicx}
\RequirePackage{xcolor}
\RequirePackage{soul}
\RequirePackage[a4paper,margin=2.5cm]{geometry}
\RequirePackage{parskip}
\RequirePackage{setspace}
\RequirePackage{pdfpages}
\RequirePackage{tocloft}
\RequirePackage{tikz}
\RequirePackage{eso-pic}
\usetikzlibrary{calc}

% ------------------------------------------------------------------
% Official Wits palette, taken from the university's own stylesheet
% (wits.ac.za/media/wits-university-style-assets/css/redesign.css)
% ------------------------------------------------------------------
\definecolor{witsnavy}{HTML}{003B5C}   % primary
\definecolor{witsgold}{HTML}{FFA300}   % primary accent
\definecolor{witsblue}{HTML}{407EC9}   % secondary
\definecolor{witsmaroon}{HTML}{9B2242} % secondary
\definecolor{witsteal}{HTML}{007377}   % secondary
\definecolor{witsgreen}{HTML}{359946}  % secondary

\setmainfont{Arial}
\newfontfamily\coverfont{Arial}

\usepackage{color,soul}
\sethlcolor{yellow}

\setlength{\parindent}{0pt}
\onehalfspacing

% --- cover page fields ---
\newcommand{\proposal}{PhD Proposal}
\newcommand{\modulecode}{Module code}
\newcommand{\schoolname}{School of Statistics and Actuarial Science}
\newcommand{\thesistitle}{Title of dissertation/thesis}
\newcommand{\initials}{Initials}
\newcommand{\surname}{Surname}
\newcommand{\studentnum}{Student number}
\newcommand{\submissiondate}{Date}

% --- title page fields ---
\newcommand{\fullnames}{Full names and surname of student}
% Overridable: a concept note is not submitted in fulfilment of a degree.
\newcommand{\proposalstatement}{Proposal submitted in fulfilment of the requirements in respect of the degree}
\newcommand{\degree}{PHILOSOPHIAE DOCTOR}
\newcommand{\proposaltype}{(Mathematical Statistics)}
\newcommand{\facultyname}{Faculty of Science}
\newcommand{\universityname}{University of the Witwatersrand}
\newcommand{\campusname}{Johannesburg, South Africa}
\newcommand{\supervisor}{Title Initials. Surname}
\newcommand{\cosupervisor}{Title Initials. Surname}
\newcommand{\proposalmonth}{Month}
\newcommand{\proposalyear}{Year}

\newcommand{\maketitlepage}{

	% =========================================================
	% Cover page: Wits navy field with gold and blue geometry,
	% white type, and the official logo on a white footer band.
	% =========================================================
	\begin{titlepage}
		\AddToShipoutPictureBG*{%
			\AtPageLowerLeft{%
				\begin{tikzpicture}[remember picture,overlay]
					% navy field over the upper three quarters
					\fill[witsnavy] (0,0.255\paperheight) rectangle (\paperwidth,\paperheight);
					% angled gold wedge
					\fill[witsgold]
					($(\paperwidth,0.255\paperheight)$) --
					($(\paperwidth,0.60\paperheight)$) --
					($(0.62\paperwidth,0.255\paperheight)$) -- cycle;
					% lighter blue wedge layered over it
					\fill[witsblue,opacity=0.92]
					($(\paperwidth,0.255\paperheight)$) --
					($(\paperwidth,0.47\paperheight)$) --
					($(0.74\paperwidth,0.255\paperheight)$) -- cycle;
					% thin gold rule separating field from footer band
					\fill[witsgold] (0,0.245\paperheight) rectangle (\paperwidth,0.255\paperheight);
					% outline motif, top left
					\draw[white,opacity=0.16,line width=2.2pt]
					(0.10\paperwidth,0.95\paperheight) circle (0.085\paperheight);
					\draw[white,opacity=0.16,line width=2.2pt]
					(0.22\paperwidth,0.95\paperheight) circle (0.085\paperheight);
				\end{tikzpicture}%
			}%
		}

		{\color{white}
			\vspace*{86pt}

			{\coverfont\fontsize{17pt}{26pt}\selectfont
				\schoolname \\
				\facultyname \\
				\proposal \\
			}

			\vspace{22pt}

			{\raggedright\begin{spacing}{1.1}
					\textbf{\fontsize{21pt}{31pt}\selectfont \thesistitle}
			\end{spacing}}

			\vspace{16pt}

			{\fontsize{16pt}{24pt}\selectfont
				\initials\ \surname \space (\studentnum)\\[-0.30cm]
				{\color{witsgold}\rule{14cm}{1.2pt}}\\[0.5cm]
				\submissiondate
			}
		}

		\vfill

		% white footer band carries the official colour logo
		\begin{center}
			\includegraphics[width=9.2cm]{template_images/wits_logo.pdf}
		\end{center}
		\vspace*{10pt}
	\end{titlepage}

	% =========================================================
	% Formal title page
	% =========================================================
	\begin{titlepage}
		\centering

		{\fontsize{14}{21}\selectfont

			\textbf{\fontsize{18}{12}\selectfont \thesistitle}

			by \\
			\fullnames \\
			{\fontsize{12.5pt}{18.75pt}\selectfont\null}

			\proposalstatement \\
			{\fontsize{12.5pt}{19.5pt}\selectfont\null}

			\textbf{\degree} \\
			\textbf{\proposaltype} \\
			{\fontsize{15pt}{22.5pt}\selectfont\null}

			in the \schoolname \\
			in the \facultyname \\
			at the \universityname \\
		}

		\rule{0pt}{22.5pt}

		\includegraphics[width=7.4cm]{template_images/wits_logo.pdf}

		\vspace*{14pt}

		\campusname\\
		\proposalmonth\ \proposalyear

		{\fontsize{12pt}{14pt}\selectfont\null}

		Student number: \studentnum \\
		Supervisor: \supervisor \\
		Co-supervisor: \cosupervisor

	\end{titlepage}
	\pagebreak
}
