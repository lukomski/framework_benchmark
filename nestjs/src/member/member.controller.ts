import { Controller, Get, Post, Body, Patch, Param, Delete, Query } from '@nestjs/common';
import { MemberService } from './member.service';
import { CreateMemberDto } from './dto/create-member.dto';
import { UpdateMemberDto } from './dto/update-member.dto';
import { ApiQuery } from '@nestjs/swagger';

@Controller('member')
export class MemberController {
  constructor(private readonly memberService: MemberService) {}

  @Post()
  create(@Body() createMemberDto: CreateMemberDto) {
    return this.memberService.create(createMemberDto);
  }

  @Get()
  findAll() {
    return this.memberService.findAll();
  }

  @Get(':id')
  findOne(@Param('id') id: string) {
    return this.memberService.findOne(+id);
  }

  @Patch(':id')
  update(@Param('id') id: string, @Body() updateMemberDto: UpdateMemberDto) {
    return this.memberService.update(+id, updateMemberDto);
  }

  @Delete(':id')
  remove(@Param('id') id: string) {
    return this.memberService.remove(+id);
  }

  @Post('clear')
  clear() {
    return this.memberService.removeAll();
  }

  @Post('fill-in')
  @ApiQuery({
    name: "N",
    type: Number,
    description: "Quantity of the entities to be added.",
    required: false
  })
  fillIn(@Query('N') n: number = 10) {
    for (let i = 0; i < n; i++) {
      this.memberService.create({name: `Name ${i}`});
    }
    return 'Ok'
  }
}
