using MediatR;
using LearnHub.Back.Application.DTOs;

namespace LearnHub.Back.Application.Handlers.Course
{
    public class GetMostDemandedCoursesQuery : IRequest<List<CourseDto>>
    {
        public int Top { get; set; } = 10; // Default to top 10 courses
    }
}
