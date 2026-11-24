from PIL import Image
import os

def image_processor():
    print("=== IMAGE PROCESSOR ===")
    print("1. Resize Image")
    print("2. Convert to Grayscale (Black & White)")
    print("3. Rotate Image")
    print("4. Blur / Crop Image")

    path = input("\nImage file peru ivvu (ex: photo.jpg): ")

    try:
        img = Image.open(path)
        print(f"\nOriginal Size: {img.size}")

        choice = input("Em cheyyali? 1/2/3/4 ivvu: ")

        if choice == "1":
            w = int(input("Kotha Width ivvu: "))
            h = int(input("Kotha Height ivvu: "))
            img = img.resize((w, h))
            img.save("resized_" + path)
            print("Resized Ayipoyindhi! ✅")

        elif choice == "2":
            img = img.convert("L")
            img.save("grayscale_" + path)
            print("Black & White Ayipoyindhi! ✅")

        elif choice == "3":
            angle = int(input("Entha degrees thippali? ex: 90: "))
            img = img.rotate(angle)
            img.save("rotated_" + path)
            print("Rotate Ayipoyindhi! ✅")

        elif choice == "4":
            # Center nunchi crop
            w, h = img.size
            img = img.crop((w//4, h//4, w*3//4, h*3//4))
            img.save("cropped_" + path)
            print("Crop Ayipoyindhi! ✅")

        else:
            print("Wrong choice!")

        print("File save ayipoyindhi!")

    except FileNotFoundError:
        print("Aa peru tho image ledhu! Peru correct ga ivvu.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    image_processor()
