#!/usr/bin/env bash
# Downloads and extracts resources
pushd
mkdir -p resources && cd $_
curl https://kenney.nl/media/pages/assets/platformer-art-deluxe/e6db792010-1677696393/kenney_platformer-art-deluxe.zip | jar xv
popd