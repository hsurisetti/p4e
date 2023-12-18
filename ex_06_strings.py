#ex_6.5
#6.5 Write code using find() and string slicing (see section 6.10) 
#to extract the number at the end of the line below. 
#Convert the extracted value to a floating point number and print it out. 


text = "X-DSPAM-Confidence:    0.8475"

# Find the position of the numerical value
start_pos = text.find(':')
end_pos = len(text)

# Extract the numerical value using string slicing
value_str = text[start_pos + 1:end_pos].strip()

# Convert the extracted string to a floating-point number
confidence_value = float(value_str)

# Print the result
print(confidence_value)

