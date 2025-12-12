using AutoMapper;
using LearnHub.Back.Application.DTOs;
using LearnHub.Back.Infrastructure;
using MediatR;
using Microsoft.EntityFrameworkCore;

namespace LearnHub.Back.Application.Handlers.Course
{
    public class GetMostDemandedCoursesQueryHandler : IRequestHandler<GetMostDemandedCoursesQuery, List<CourseDto>>
    {
        private readonly ApplicationDbContext _context;
        private readonly IMapper _mapper;

        public GetMostDemandedCoursesQueryHandler(ApplicationDbContext context, IMapper mapper)
        {
            _context = context;
            _mapper = mapper;
        }

        public async Task<List<CourseDto>> Handle(GetMostDemandedCoursesQuery request, CancellationToken cancellationToken)
        {
            var courseIds = await _context.Courses
                .Select(c => new { c.Id, EnrollmentCount = c.Enrollments.Count })
                .OrderByDescending(x => x.EnrollmentCount)
                .Take(request.Top)
                .Select(x => x.Id)
                .ToListAsync(cancellationToken);

            var courses = await _context.Courses
                .Include(c => c.Instructor)
                .Include(c => c.Enrollments)
                .Where(c => courseIds.Contains(c.Id))
                .ToListAsync(cancellationToken);

            // Maintain the order based on enrollment count
            var orderedCourses = courseIds
                .Select(id => courses.First(c => c.Id == id))
                .ToList();

            return _mapper.Map<List<CourseDto>>(orderedCourses);
        }
    }
}
