#!/usr/bin/env python3

import aws_cdk

from cdk.smart_gallery.smart_gallery_stack import SmartGalleryStack


app = aws_cdk.App()
SmartGalleryStack(app, "SmartGalleryStack")

app.synth()
