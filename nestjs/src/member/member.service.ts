import { Injectable } from '@nestjs/common';
import { CreateMemberDto } from './dto/create-member.dto';
import { UpdateMemberDto } from './dto/update-member.dto';
import { Member } from './entities/member.entity';
import { InjectRepository } from '@nestjs/typeorm';
import { DeleteResult, Repository, UpdateResult } from 'typeorm';

@Injectable()
export class MemberService {
  constructor(
    @InjectRepository(Member)
    private readonly memberRepository: Repository<Member>,
  ) {}

  create(createMemberDto: CreateMemberDto): Promise<Member> {
    const member: Member = new Member();
    member.name = createMemberDto.name;
    return this.memberRepository.save(member);
  }

  findAll(): Promise<Member[]> {
    return this.memberRepository.find();
  }

  findOne(id: number): Promise<Member | null> {
    return this.memberRepository.findOneBy({ id });
  }

  update(id: number, updateMemberDto: UpdateMemberDto): Promise<UpdateResult> {
    const member: Member = new Member();
    member.name = updateMemberDto.name;
    member.id = id;
    return this.memberRepository.update(id, member);
  }

  remove(id: number): Promise<DeleteResult> {
    return this.memberRepository.delete(id);
  }

  removeAll(): Promise<void> {
    return this.memberRepository.clear()
  }
}
