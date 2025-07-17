import json
import os
import random
import argparse
import numpy as np
from transformers import (
    AutoTokenizer, AutoModelForSequenceClassification,
    Trainer, TrainingArguments, DataCollatorWithPadding
)
from datasets import Dataset
import torch

# ---------------------------
# Seed Setting for Reproducibility
# ---------------------------
def set_seed(seed=42):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)

# ---------------------------
# Load and Prepare Data
# ---------------------------
def load_data(jsonl_path):
    with open(jsonl_path, 'r') as f:
        lines = [json.loads(line) for line in f]
    texts = [line["text"] for line in lines]
    labels = [1 if line["label"] == "positive" else 0 for line in lines]
    return Dataset.from_dict({"text": texts, "label": labels})

# ---------------------------
# Main Fine-Tuning Function
# ---------------------------
def main(args):
    set_seed()

    model_name = "distilbert-base-uncased"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)

    dataset = load_data(args.data)

    # Tokenize the dataset
    def tokenize(batch):
        return tokenizer(batch["text"], truncation=True)

    dataset = dataset.map(tokenize, batched=True)

    # Define training arguments (no eval, so no load_best_model_at_end)
    training_args = TrainingArguments(
        output_dir="./model",
        per_device_train_batch_size=8,
        num_train_epochs=args.epochs,
        learning_rate=args.lr,
        logging_dir='./logs',
        save_total_limit=1
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset,
        tokenizer=tokenizer,
        data_collator=DataCollatorWithPadding(tokenizer),
    )

    trainer.train()

    # Save the fine-tuned model and tokenizer
    model.save_pretrained("./model")
    tokenizer.save_pretrained("./model")
    print("✅ Model saved to ./model")

# ---------------------------
# Argument Parser
# ---------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True, help="Path to JSONL dataset")
    parser.add_argument("--epochs", type=int, default=3)
    parser.add_argument("--lr", type=float, default=3e-5)
    args = parser.parse_args()
    main(args)
