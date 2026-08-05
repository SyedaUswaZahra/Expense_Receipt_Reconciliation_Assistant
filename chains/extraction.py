llm=llm, parser=PydanticOutputParser(pydantic_object=ReceiptSchema, chain=EXTRACT_RECEIPT_PROMPT, image_bytes=f.read(, image_b64=base64.b64encode(image_bytes, messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Extract the receipt data from this image."},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{image_b64}"},
                    },
                ],
            }
        ], response=self.chain.invoke(