#!/bin/bash

for filename in most_2000/valid_old/*.JPEG; do
        fnew=${filename/valid_old/valid}
        cp $filename ${fnew/.JPEG/_old.JPEG}
done

for filename in most_2000/valid_new/*.JPEG; do
        fnew=${filename/valid_new/valid}
        cp $filename ${fnew/.JPEG/_new.JPEG}
done