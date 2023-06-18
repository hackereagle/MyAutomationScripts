#!/bin/bash

branch=${1}
git push origin ${branch}
git push mygitlab ${branch}
