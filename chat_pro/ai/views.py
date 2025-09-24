from django.shortcuts import render
from django.conf import settings
import google.generativeai as genai
from huggingface_hub import InferenceClient
import base64

# Configure Gemini
genai.configure(api_key=settings.GEMINI_API_KEY)

# Configure Hugging Face client
hf_client = InferenceClient(
    model="stabilityai/stable-diffusion-xl-base-1.0",
    token=settings.HF_API_KEY
)

# Gemini text generation
def text_generation(request):
    result = None
    if request.method == "POST":
        prompt = request.POST.get("prompt")
        if prompt:
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(prompt)
            result = response.text
    return render(request, "geminiapp/text.html", {"result": result})


# Stable Diffusion image generation via HF InferenceClient
def image_generation(request):
    result = None
    if request.method == "POST":
        prompt = request.POST.get("prompt")
        if prompt:
            try:
                image = hf_client.text_to_image(prompt)  # returns PIL image
                # Convert PIL → base64 for HTML
                import io
                buffer = io.BytesIO()
                image.save(buffer, format="PNG")
                encoded = base64.b64encode(buffer.getvalue()).decode("utf-8")
                result = f"data:image/png;base64,{encoded}"
            except Exception as e:
                result = f"Error: {str(e)}"

    return render(request, "geminiapp/image.html", {"result": result})
