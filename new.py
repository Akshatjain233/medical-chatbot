import time

qna = {
  "hi": "heyy",
  "what are your store timings?": "Our store is open from 9 AM to 9 PM, Monday to Saturday.",
  "do you deliver medicines at home?": "Yes, we offer home delivery within city limits.",
  "can I buy medicines without a prescription?": "Prescription is required for all scheduled drugs.",
  "do you sell ayurvedic medicines?": "Yes, we have a range of ayurvedic and herbal medicines.",
  "how can I place an order?": "You can call us, WhatsApp us, or visit our website to place an order.",
  "do you accept online payments?": "Yes, we accept UPI, credit/debit cards, and net banking.",
  "is there a discount on bulk purchases?": "Yes, we offer discounts on bulk and repeat purchases.",
  "can I return expired medicines?": "We do not accept returns on expired medicines.",
  "do you have a pharmacist available for consultation?": "Yes, our licensed pharmacist is available during store hours."
};
while True:
    ques = input()

    if (ques=="quit"):
        break
    else :
        print(qna[ques])