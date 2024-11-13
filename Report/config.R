working_directory <- "C:/Users/bayop/Documents/Statistique_R/Bootcamp_FR1/Bootcamp_FR1/Report/"

# Fonction pour installer et charger les packages
install_and_load_packages <- function(packages) {
  for (pkg in packages) {
    if (!require(pkg, character.only = TRUE)) {
      install.packages(pkg, dependencies = TRUE)
      library(pkg, character.only = TRUE)
    }
  }
}
#fig.cap="Tendance des températures moyenne annuelles en France"

