#!/usr/bin/env python3

import aws_cdk

from smart_gallery.smart_gallery_stack import SmartGalleryStack


app = aws_cdk.App()
SmartGalleryStack(app, "SmartGalleryStack")

app.synth()
