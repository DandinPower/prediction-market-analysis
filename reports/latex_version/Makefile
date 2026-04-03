TEX_NAME = main
REFERENCES_NAME = references
IMAGES_DIR = images
BUILD_DIR = build

all:
	mkdir -p ${BUILD_DIR}
	cp $(TEX_NAME).tex ${REFERENCES_NAME}.bib ${BUILD_DIR}
	cp -r ${IMAGES_DIR} ${BUILD_DIR}
	cd ${BUILD_DIR} && pdflatex $(TEX_NAME).tex
	cd ${BUILD_DIR} && bibtex $(TEX_NAME)
	cd ${BUILD_DIR} && pdflatex $(TEX_NAME).tex
	cd ${BUILD_DIR} && pdflatex $(TEX_NAME).tex

clean:
	rm -rf ${BUILD_DIR}