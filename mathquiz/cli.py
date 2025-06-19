import argparse
from .core import Quiz

def main():
    parser = argparse.ArgumentParser(description="Gera um quiz de aritmética.")
    parser.add_argument("--num", type=int, default=10)
    parser.add_argument("--ops", nargs="+", default=["+", "-", "*", "/"])
    parser.add_argument("--min", type=float, default=1)
    parser.add_argument("--max", type=float, default=10)
    parser.add_argument("--decimals", action="store_true")
    parser.add_argument("--places", type=int, default=2)

    args = parser.parse_args()
    quiz = Quiz(
        num_questions=args.num,
        operations=args.ops,
        min_val=args.min,
        max_val=args.max,
        use_decimals=args.decimals,
        decimal_places=args.places
    )
    quiz.run()
    quiz.display_report()

if __name__ == "__main__":
    main()
