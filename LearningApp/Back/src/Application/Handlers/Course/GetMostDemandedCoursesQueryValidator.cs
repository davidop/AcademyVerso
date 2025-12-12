using FluentValidation;

namespace LearnHub.Back.Application.Handlers.Course
{
    public class GetMostDemandedCoursesQueryValidator : AbstractValidator<GetMostDemandedCoursesQuery>
    {
        public GetMostDemandedCoursesQueryValidator()
        {
            RuleFor(x => x.Top)
                .GreaterThan(0)
                .WithMessage("Top must be greater than 0")
                .LessThanOrEqualTo(100)
                .WithMessage("Top must not exceed 100");
        }
    }
}
