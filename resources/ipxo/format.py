# Вкажіть шлях до вашого файлу geofeed
input_file = "geofeed.txt"
output_file = "formatted_geofeed.txt"

# Відкриваємо вхідний файл
with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    for line in infile:
        # Пропускаємо порожні рядки та коментарі
        if line.strip() == "" or line.startswith("#"):
            continue
        
        # Розділяємо рядок за комою
        parts = line.strip().split(",")
        
        if len(parts) >= 2:
            prefix = parts[0].strip()
            comment = " ".join(parts[1:]).strip()
            
            # Форматуємо рядок як "префікс два таби коментар"
            formatted_line = f"{prefix}\t\t# {comment}\n"
            outfile.write(formatted_line)

print(f"Файл збережено як {output_file}")
